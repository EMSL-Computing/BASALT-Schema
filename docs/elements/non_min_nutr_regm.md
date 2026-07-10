

# Slot: non mineral nutrient regimen (non_min_nutr_regm) 


_Information about treatment involving the exposure of plant to non-mineral nutrient such as oxygen, hydrogen, or carbon; should include the name of non-mineral nutrient, amount administered, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple non-mineral nutrient regimens_





URI: [analysis_api_schema:non_min_nutr_regm](https://w3id.org/MONet/analysis-api-schema/non_min_nutr_regm)
Alias: non_min_nutr_regm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:non_min_nutr_regm |
| native | analysis_api_schema:non_min_nutr_regm |




## LinkML Source

<details>
```yaml
name: non_min_nutr_regm
description: Information about treatment involving the exposure of plant to non-mineral
  nutrient such as oxygen, hydrogen, or carbon; should include the name of non-mineral
  nutrient, amount administered, treatment regimen including how many times the treatment
  was repeated, how long each treatment lasted, and the start and end time of the
  entire treatment; can include multiple non-mineral nutrient regimens
title: non mineral nutrient regimen
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: non_min_nutr_regm
domain_of:
- FieldDeployedTerraformSample
- OtherUndescribedSample
- PlantSample
- TerraformSample
range: string

```
</details>