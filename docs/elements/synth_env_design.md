

# Slot: synthetic environment design (synth_env_design) 


_The design of the synthetic environment that was created for experimentation_





URI: [analysis_api_schema:synth_env_design](https://w3id.org/MONet/analysis-api-schema/synth_env_design)
Alias: synth_env_design

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |







## Properties

* Range: [SyntheticEnvironmentEnum](SyntheticEnvironmentEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:synth_env_design |
| native | analysis_api_schema:synth_env_design |




## LinkML Source

<details>
```yaml
name: synth_env_design
description: The design of the synthetic environment that was created for experimentation
title: synthetic environment design
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: synth_env_design
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: SyntheticEnvironmentEnum

```
</details>