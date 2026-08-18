

# Slot: host genotype (host_genotype) 


_Observed genotype_





URI: [basalt_schema:host_genotype](https://EMSL-Computing.github.io/BASALT-Schema/host_genotype)
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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_genotype |
| native | basalt_schema:host_genotype |




## LinkML Source

<details>
```yaml
name: host_genotype
description: Observed genotype
title: host genotype
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: host_genotype
domain_of:
- FieldDeployedTerraformSample
- TerraformSample
range: string

```
</details>