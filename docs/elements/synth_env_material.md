

# Slot: synthetic environment material (synth_env_material) 


_Describes the fabrication material used to create the synthetic environment and what the structure is made of_





URI: [basalt_schema:synth_env_material](https://EMSL-Computing.github.io/BASALT-Schema/synth_env_material)
Alias: synth_env_material

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |






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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_env_material |
| native | basalt_schema:synth_env_material |




## LinkML Source

<details>
```yaml
name: synth_env_material
description: Describes the fabrication material used to create the synthetic environment
  and what the structure is made of
title: synthetic environment material
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: synth_env_material
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>