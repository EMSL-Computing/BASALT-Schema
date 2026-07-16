

# Slot: mineral nutrient regimen (mineral_nutr_regm) 


_Information about treatment involving the use of mineral supplements; should include the name of mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple mineral nutrient regimens_





URI: [analysis_api_schema:mineral_nutr_regm](https://w3id.org/MONet/analysis-api-schema/mineral_nutr_regm)
Alias: mineral_nutr_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






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
| self | analysis_api_schema:mineral_nutr_regm |
| native | analysis_api_schema:mineral_nutr_regm |




## LinkML Source

<details>
```yaml
name: mineral_nutr_regm
description: Information about treatment involving the use of mineral supplements;
  should include the name of mineral nutrient, amount administered, treatment regimen
  including how many times the treatment was repeated, how long each treatment lasted,
  and the start and end time of the entire treatment; can include multiple mineral
  nutrient regimens
title: mineral nutrient regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: mineral_nutr_regm
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- PlantSample
- TerraformSample
range: string

```
</details>