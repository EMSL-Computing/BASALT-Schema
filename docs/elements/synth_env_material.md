

# Slot: synthetic environment material (synth_env_material) 


_Describes the fabrication material used to create the synthetic environment and what the structure is made of_





URI: [analysis_api_schema:synth_env_material](https://w3id.org/MONet/analysis-api-schema/synth_env_material)
Alias: synth_env_material

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:synth_env_material |
| native | analysis_api_schema:synth_env_material |




## LinkML Source

<details>
```yaml
name: synth_env_material
description: Describes the fabrication material used to create the synthetic environment
  and what the structure is made of
title: synthetic environment material
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: synth_env_material
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>