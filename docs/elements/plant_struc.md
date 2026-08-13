

# Slot: plant structure (plant_struc) 


_Name of plant structure the sample was obtained from; for Plant Ontology (PO) (v releases/2017-12-14) terms see http://purl.bioontology.org/ontology/PO e.g. petiole epidermis (PO_0000051). If an individual flower is sampled the sex of it can be recorded here._





URI: [basalt_schema:plant_struc](https://EMSL-Computing.github.io/basalt-schema/plant_struc)
Alias: plant_struc

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PlantStructureEnum](PlantStructureEnum.md) |
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
| self | basalt_schema:plant_struc |
| native | basalt_schema:plant_struc |




## LinkML Source

<details>
```yaml
name: plant_struc
description: Name of plant structure the sample was obtained from; for Plant Ontology
  (PO) (v releases/2017-12-14) terms see http://purl.bioontology.org/ontology/PO e.g.
  petiole epidermis (PO_0000051). If an individual flower is sampled the sex of it
  can be recorded here.
title: plant structure
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: plant_struc
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: PlantStructureEnum

```
</details>