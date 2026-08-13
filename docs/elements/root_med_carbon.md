

# Slot: rooting medium carbon (root_med_carbon) 


_Source of organic carbon in the culture rooting medium. Provide as {carbon source}, {value}{unit}. Can be multivalued, separated by ;. Preferred unit mg/L._





URI: [basalt_schema:root_med_carbon](https://EMSL-Computing.github.io/basalt-schema/root_med_carbon)
Alias: root_med_carbon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






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


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:root_med_carbon |
| native | basalt_schema:root_med_carbon |




## LinkML Source

<details>
```yaml
name: root_med_carbon
description: Source of organic carbon in the culture rooting medium. Provide as {carbon
  source}, {value}{unit}. Can be multivalued, separated by ;. Preferred unit mg/L.
title: rooting medium carbon
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: root_med_carbon
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>