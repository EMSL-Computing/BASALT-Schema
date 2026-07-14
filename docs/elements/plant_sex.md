

# Slot: plant sex (plant_sex) 


_Sex of the reproductive parts on the whole plant._





URI: [analysis_api_schema:plant_sex](https://w3id.org/MONet/analysis-api-schema/plant_sex)
Alias: plant_sex

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [PlantSexEnum](PlantSexEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plant_sex |
| native | analysis_api_schema:plant_sex |




## LinkML Source

<details>
```yaml
name: plant_sex
description: Sex of the reproductive parts on the whole plant.
title: plant sex
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plant_sex
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: PlantSexEnum

```
</details>