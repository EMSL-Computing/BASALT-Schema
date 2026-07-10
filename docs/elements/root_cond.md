

# Slot: rooting conditions (root_cond) 


_Relevant rooting conditions such as field plot size, sowing density, container dimensions, number of plants per container._





URI: [analysis_api_schema:root_cond](https://w3id.org/MONet/analysis-api-schema/root_cond)
Alias: root_cond

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:root_cond |
| native | analysis_api_schema:root_cond |




## LinkML Source

<details>
```yaml
name: root_cond
description: Relevant rooting conditions such as field plot size, sowing density,
  container dimensions, number of plants per container.
title: rooting conditions
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: root_cond
domain_of:
- FieldDeployedTerraformSample
- PlantSample
- TerraformSample
range: string

```
</details>