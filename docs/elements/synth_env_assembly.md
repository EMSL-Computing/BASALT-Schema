

# Slot: synthetic environment assembly (synth_env_assembly) 


_Describes how the synthetic environments parts are contained and assembled_





URI: [basalt_schema:synth_env_assembly](https://emsl-computing.github.io/BASALT-Schema/elements/synth_env_assembly)
Alias: synth_env_assembly

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_env_assembly |
| native | basalt_schema:synth_env_assembly |




## LinkML Source

<details>
```yaml
name: synth_env_assembly
description: Describes how the synthetic environments parts are contained and assembled
title: synthetic environment assembly
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: synth_env_assembly
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>