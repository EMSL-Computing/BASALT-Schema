

# Slot: rooting medium micronutrients (root_med_micronutr) 


_Measurement of the culture rooting medium micronutrients (Fe Mn Zn B Cu Mo). Can be multivalued separated by ;. e.g. H3BO3 6.2 mg/L_





URI: [basalt_schema:root_med_micronutr](https://w3id.org/MONet/basalt-schema/root_med_micronutr)
Alias: root_med_micronutr

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:root_med_micronutr |
| native | basalt_schema:root_med_micronutr |




## LinkML Source

<details>
```yaml
name: root_med_micronutr
description: Measurement of the culture rooting medium micronutrients (Fe Mn Zn B
  Cu Mo). Can be multivalued separated by ;. e.g. H3BO3 6.2 mg/L
title: rooting medium micronutrients
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: root_med_micronutr
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>