

# Slot: synthetic environment assembly (synth_env_assembly) 


_Describes how the synthetic environments parts are contained and assembled_





URI: [analysis_api_schema:synth_env_assembly](https://w3id.org/MONet/analysis-api-schema/synth_env_assembly)
Alias: synth_env_assembly

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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:synth_env_assembly |
| native | analysis_api_schema:synth_env_assembly |




## LinkML Source

<details>
```yaml
name: synth_env_assembly
description: Describes how the synthetic environments parts are contained and assembled
title: synthetic environment assembly
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: synth_env_assembly
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>