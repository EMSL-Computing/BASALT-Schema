

# Slot: gaseous environment (gaseous_environment) 


_Use of conditions with differing gaseous environments; should include the name of gaseous compound, amount administered, treatment duration, interval, and total experimental duration; can include multiple gaseous environment regimens_





URI: [analysis_api_schema:gaseous_environment](https://w3id.org/MONet/analysis-api-schema/gaseous_environment)
Alias: gaseous_environment

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:gaseous_environment |
| native | analysis_api_schema:gaseous_environment |




## LinkML Source

<details>
```yaml
name: gaseous_environment
description: Use of conditions with differing gaseous environments; should include
  the name of gaseous compound, amount administered, treatment duration, interval,
  and total experimental duration; can include multiple gaseous environment regimens
title: gaseous environment
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: gaseous_environment
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- TerraformSample
- WaterSample
range: string

```
</details>