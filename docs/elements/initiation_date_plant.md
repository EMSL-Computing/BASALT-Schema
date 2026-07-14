

# Slot: initiation date of plant (initiation_date_plant) 


_The date the plant part of the sample was initiated. This can be the date of germination or propagation. If providing a sequential initiation (propagation), the sample should be linked to the sample it originated from. Formatted as YYYY-MM-DD_





URI: [analysis_api_schema:initiation_date_plant](https://w3id.org/MONet/analysis-api-schema/initiation_date_plant)
Alias: initiation_date_plant

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
| self | analysis_api_schema:initiation_date_plant |
| native | analysis_api_schema:initiation_date_plant |




## LinkML Source

<details>
```yaml
name: initiation_date_plant
description: The date the plant part of the sample was initiated. This can be the
  date of germination or propagation. If providing a sequential initiation (propagation),
  the sample should be linked to the sample it originated from. Formatted as YYYY-MM-DD
title: initiation date of plant
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: initiation_date_plant
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string
pattern: ^[12]\d{3}(?:(?:-(?:0[1-9]|1[0-2]))(?:-(?:0[1-9]|[12]\d|3[01]))?)?$

```
</details>