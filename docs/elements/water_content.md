

# Slot: water content (water_content) 


_Water content measurement. Provide value and unit any unit is valid_





URI: [analysis_api_schema:water_content](https://w3id.org/MONet/analysis-api-schema/water_content)
Alias: water_content

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+(\.\d+)?\s*[\w\s/]+$`





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:water_content |
| native | analysis_api_schema:water_content |




## LinkML Source

<details>
```yaml
name: water_content
description: Water content measurement. Provide value and unit any unit is valid
title: water content
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: water_content
domain_of:
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- SedimentSample
- SoilSample
- TerraformSample
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>