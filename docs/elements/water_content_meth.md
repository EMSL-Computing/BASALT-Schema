

# Slot: water content method (water_content_meth) 


_Reference or method used in determining the water content of soil_





URI: [analysis_api_schema:water_content_meth](https://w3id.org/MONet/analysis-api-schema/water_content_meth)
Alias: water_content_meth

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:water_content_meth |
| native | analysis_api_schema:water_content_meth |




## LinkML Source

<details>
```yaml
name: water_content_meth
description: Reference or method used in determining the water content of soil
title: water content method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: water_content_meth
domain_of:
- FieldDeployedTerraformSample
- MonetSoilSample
- SedimentSample
- SoilSample
- TerraformSample
range: string

```
</details>