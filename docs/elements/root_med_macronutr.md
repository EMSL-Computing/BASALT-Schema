

# Slot: rooting medium macronutrients (root_med_macronutr) 


_Measurement of the culture rooting medium macronutrients (NP K Ca Mg S). Can be multivalued separated by ;. e.g. KH2PO4 170 mg/L_





URI: [analysis_api_schema:root_med_macronutr](https://w3id.org/MONet/analysis-api-schema/root_med_macronutr)
Alias: root_med_macronutr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:root_med_macronutr |
| native | analysis_api_schema:root_med_macronutr |




## LinkML Source

<details>
```yaml
name: root_med_macronutr
description: Measurement of the culture rooting medium macronutrients (NP K Ca Mg
  S). Can be multivalued separated by ;. e.g. KH2PO4 170 mg/L
title: rooting medium macronutrients
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: root_med_macronutr
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>