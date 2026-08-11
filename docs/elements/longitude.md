

# Slot: longitude (longitude) 


_Longitude coordinate of the sampling site in WSG 84 format._





URI: [basalt_schema:longitude](https://w3id.org/MONet/basalt-schema/longitude)
Alias: longitude

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [Site](Site.md) | Site-level metadata for a specific location from which a set of samples are c... |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |






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


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:longitude |
| native | basalt_schema:longitude |
| broad | MIXS:0000009 |




## LinkML Source

<details>
```yaml
name: longitude
description: Longitude coordinate of the sampling site in WSG 84 format.
title: longitude
from_schema: https://w3id.org/MONet/basalt-schema
broad_mappings:
- MIXS:0000009
rank: 1000
alias: longitude
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