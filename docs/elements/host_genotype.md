

# Slot: host genotype (host_genotype) 


_Observed genotype_





URI: [analysis_api_schema:host_genotype](https://w3id.org/MONet/analysis-api-schema/host_genotype)
Alias: host_genotype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






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
| self | analysis_api_schema:host_genotype |
| native | analysis_api_schema:host_genotype |




## LinkML Source

<details>
```yaml
name: host_genotype
description: Observed genotype
title: host genotype
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: host_genotype
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>