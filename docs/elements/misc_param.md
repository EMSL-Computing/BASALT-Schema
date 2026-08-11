

# Slot: miscellaneous parameter (misc_param) 


_Any other measurement performed or parameter collected that is not listed here_





URI: [basalt_schema:misc_param](https://EMSL-Computing.github.io/basalt-schema/misc_param)
Alias: misc_param

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:misc_param |
| native | basalt_schema:misc_param |




## LinkML Source

<details>
```yaml
name: misc_param
description: Any other measurement performed or parameter collected that is not listed
  here
title: miscellaneous parameter
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: misc_param
domain_of:
- AerosolArmSample
- AerosolSample
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- TerraformSample
- WaterSample
range: string

```
</details>