

# Slot: rooting medium macronutrients (root_med_macronutr) 


_Measurement of the culture rooting medium macronutrients (NP K Ca Mg S). Can be multivalued separated by ;. e.g. KH2PO4 170 mg/L_





URI: [basalt_schema:root_med_macronutr](https://EMSL-Computing.github.io/BASALT-Schema/root_med_macronutr)
Alias: root_med_macronutr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [PlantSample](PlantSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:root_med_macronutr |
| native | basalt_schema:root_med_macronutr |




## LinkML Source

<details>
```yaml
name: root_med_macronutr
description: Measurement of the culture rooting medium macronutrients (NP K Ca Mg
  S). Can be multivalued separated by ;. e.g. KH2PO4 170 mg/L
title: rooting medium macronutrients
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: root_med_macronutr
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>