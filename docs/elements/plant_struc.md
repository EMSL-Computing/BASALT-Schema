

# Slot: plant structure (plant_struc) 


_Name of plant structure the sample was obtained from; for Plant Ontology (PO) (v releases/2017-12-14) terms see http://purl.bioontology.org/ontology/PO e.g. petiole epidermis (PO_0000051). If an individual flower is sampled the sex of it can be recorded here._





URI: [analysis_api_schema:plant_struc](https://w3id.org/MONet/analysis-api-schema/plant_struc)
Alias: plant_struc

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [PlantStructureEnum](PlantStructureEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plant_struc |
| native | analysis_api_schema:plant_struc |




## LinkML Source

<details>
```yaml
name: plant_struc
description: Name of plant structure the sample was obtained from; for Plant Ontology
  (PO) (v releases/2017-12-14) terms see http://purl.bioontology.org/ontology/PO e.g.
  petiole epidermis (PO_0000051). If an individual flower is sampled the sex of it
  can be recorded here.
title: plant structure
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plant_struc
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: PlantStructureEnum

```
</details>