

# Slot: latitude (latitude) 


_Latitude coordinate of the sampling site in WSG 84 format._





URI: [analysis_api_schema:latitude](https://w3id.org/MONet/analysis-api-schema/latitude)
Alias: latitude

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [Site](Site.md), [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:latitude |
| native | analysis_api_schema:latitude |
| broad | MIXS:0000009 |




## LinkML Source

<details>
```yaml
name: latitude
description: Latitude coordinate of the sampling site in WSG 84 format.
title: latitude
from_schema: https://w3id.org/MONet/analysis-api-schema
broad_mappings:
- MIXS:0000009
rank: 1000
alias: latitude
domain_of:
- Site
- AerosolArmSample
- AerosolSample
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- WaterSample
range: double

```
</details>