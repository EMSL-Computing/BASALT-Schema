

# Slot: synthetic environment treatment (synth_env_treatment) 


_Describes any treatments that are built into the synthetic environment_





URI: [basalt_schema:synth_env_treatment](https://EMSL-Computing.github.io/basalt-schema/synth_env_treatment)
Alias: synth_env_treatment

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
| self | basalt_schema:synth_env_treatment |
| native | basalt_schema:synth_env_treatment |




## LinkML Source

<details>
```yaml
name: synth_env_treatment
description: Describes any treatments that are built into the synthetic environment
title: synthetic environment treatment
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: synth_env_treatment
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>