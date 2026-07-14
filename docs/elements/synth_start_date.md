

# Slot: synthetic environment start date (synth_start_date) 


_Provide the date the sample was transferred to the synthetic environment. Formatted as YYYY-MM-DD_





URI: [analysis_api_schema:synth_start_date](https://w3id.org/MONet/analysis-api-schema/synth_start_date)
Alias: synth_start_date

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:synth_start_date |
| native | analysis_api_schema:synth_start_date |




## LinkML Source

<details>
```yaml
name: synth_start_date
description: Provide the date the sample was transferred to the synthetic environment.
  Formatted as YYYY-MM-DD
title: synthetic environment start date
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: synth_start_date
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>