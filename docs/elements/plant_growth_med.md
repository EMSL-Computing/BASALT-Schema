

# Slot: plant growth medium (plant_growth_med) 


_Specification of the media for growing the plants or tissue cultured samples e.g. soil, aeroponic, hydroponic, in vitro, solid culture medium, in vitro, liquid culture medium. Value is required to be a subclass from the PECO ontology (http://purl.bioontology.org/ontology/PECO). The value should be formatted as the name of the media followed by the PECO identifier in brackets, e.g. aeroponic plant growth media exposure [PECO:0001073]_





URI: [analysis_api_schema:plant_growth_med](https://w3id.org/MONet/analysis-api-schema/plant_growth_med)
Alias: plant_growth_med

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^_*\s*[a-zA-Z\s]+\[PECO:\d+\]$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:plant_growth_med |
| native | analysis_api_schema:plant_growth_med |




## LinkML Source

<details>
```yaml
name: plant_growth_med
description: Specification of the media for growing the plants or tissue cultured
  samples e.g. soil, aeroponic, hydroponic, in vitro, solid culture medium, in vitro,
  liquid culture medium. Value is required to be a subclass from the PECO ontology
  (http://purl.bioontology.org/ontology/PECO). The value should be formatted as the
  name of the media followed by the PECO identifier in brackets, e.g. aeroponic plant
  growth media exposure [PECO:0001073]
title: plant growth medium
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: plant_growth_med
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string
pattern: ^_*\s*[a-zA-Z\s]+\[PECO:\d+\]$

```
</details>