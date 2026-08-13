

# Slot: rooting conditions (root_cond) 


_Relevant rooting conditions such as field plot size, sowing density, container dimensions, number of plants per container._





URI: [basalt_schema:root_cond](https://EMSL-Computing.github.io/BASALT-Schema/root_cond)
Alias: root_cond

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [PlantSample](PlantSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:root_cond |
| native | basalt_schema:root_cond |




## LinkML Source

<details>
```yaml
name: root_cond
description: Relevant rooting conditions such as field plot size, sowing density,
  container dimensions, number of plants per container.
title: rooting conditions
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: root_cond
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>