

# Slot: synthetic environment design method (synth_env_design_method) 


_A citation for how the synthetic environment was designed_





URI: [basalt_schema:synth_env_design_method](https://EMSL-Computing.github.io/basalt-schema/synth_env_design_method)
Alias: synth_env_design_method

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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:synth_env_design_method |
| native | basalt_schema:synth_env_design_method |




## LinkML Source

<details>
```yaml
name: synth_env_design_method
description: A citation for how the synthetic environment was designed
title: synthetic environment design method
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: synth_env_design_method
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>