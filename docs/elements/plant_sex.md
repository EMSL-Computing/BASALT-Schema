

# Slot: plant sex (plant_sex) 


_Sex of the reproductive parts on the whole plant._





URI: [basalt_schema:plant_sex](https://emsl-computing.github.io/BASALT-Schema/elements/plant_sex)
Alias: plant_sex

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PlantSexEnum](PlantSexEnum.md) |
| Domain Of | [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [PlantSample](PlantSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:plant_sex |
| native | basalt_schema:plant_sex |




## LinkML Source

<details>
```yaml
name: plant_sex
description: Sex of the reproductive parts on the whole plant.
title: plant sex
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: plant_sex
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: PlantSexEnum

```
</details>