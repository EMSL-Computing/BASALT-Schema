

# Slot: host life stage (host_life_stage) 


_Description of life stage of host_





URI: [basalt_schema:host_life_stage](https://EMSL-Computing.github.io/basalt-schema/host_life_stage)
Alias: host_life_stage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_life_stage |
| native | basalt_schema:host_life_stage |




## LinkML Source

<details>
```yaml
name: host_life_stage
description: Description of life stage of host
title: host life stage
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: host_life_stage
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- PlantSample
- TerraformSample
range: string

```
</details>