

# Slot: host life stage (host_life_stage) 


_Description of life stage of host_





URI: [analysis_api_schema:host_life_stage](https://w3id.org/MONet/analysis-api-schema/host_life_stage)
Alias: host_life_stage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_life_stage |
| native | analysis_api_schema:host_life_stage |




## LinkML Source

<details>
```yaml
name: host_life_stage
description: Description of life stage of host
title: host life stage
from_schema: https://w3id.org/MONet/analysis-api-schema
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