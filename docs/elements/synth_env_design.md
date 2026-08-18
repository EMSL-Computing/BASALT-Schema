

# Slot: synthetic environment design (synth_env_design) 


_The design of the synthetic environment that was created for experimentation_





URI: [basalt_schema:synth_env_design](https://emsl-computing.github.io/BASALT-Schema/elements/synth_env_design)
Alias: synth_env_design

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
| Range | [SyntheticEnvironmentEnum](SyntheticEnvironmentEnum.md) |
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
| self | basalt_schema:synth_env_design |
| native | basalt_schema:synth_env_design |




## LinkML Source

<details>
```yaml
name: synth_env_design
description: The design of the synthetic environment that was created for experimentation
title: synthetic environment design
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: synth_env_design
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: SyntheticEnvironmentEnum

```
</details>