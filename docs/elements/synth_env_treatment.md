

# Slot: synthetic environment treatment (synth_env_treatment) 


_Describes any treatments that are built into the synthetic environment_





URI: [analysis_api_schema:synth_env_treatment](https://w3id.org/MONet/analysis-api-schema/synth_env_treatment)
Alias: synth_env_treatment

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:synth_env_treatment |
| native | analysis_api_schema:synth_env_treatment |




## LinkML Source

<details>
```yaml
name: synth_env_treatment
description: Describes any treatments that are built into the synthetic environment
title: synthetic environment treatment
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: synth_env_treatment
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>