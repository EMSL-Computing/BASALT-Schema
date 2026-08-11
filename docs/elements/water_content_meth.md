

# Slot: water content method (water_content_meth) 


_Reference or method used in determining the water content of soil_





URI: [basalt_schema:water_content_meth](https://EMSL-Computing.github.io/basalt-schema/water_content_meth)
Alias: water_content_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:water_content_meth |
| native | basalt_schema:water_content_meth |




## LinkML Source

<details>
```yaml
name: water_content_meth
description: Reference or method used in determining the water content of soil
title: water content method
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: water_content_meth
domain_of:
- FieldDeployedTerraformSample
- MonetSoilSample
- SedimentSample
- SoilSample
- TerraformSample
range: string

```
</details>