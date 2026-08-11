

# Slot: plant product (plant_product) 


_Substance produced by the plant where the sample was obtained from_





URI: [basalt_schema:plant_product](https://EMSL-Computing.github.io/basalt-schema/plant_product)
Alias: plant_product

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_product |
| native | basalt_schema:plant_product |




## LinkML Source

<details>
```yaml
name: plant_product
description: Substance produced by the plant where the sample was obtained from
title: plant product
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: plant_product
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>