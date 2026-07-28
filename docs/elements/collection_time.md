

# Slot: collection time (collection_time) 


_The time of sampling as an instance (single point). Required format: HH:MM:SS in 24-hour time format. Don't forget the second! (Unit: hh:mm:ss or HH:MM:SS)_





URI: [analysis_api_schema:collection_time](https://w3id.org/MONet/analysis-api-schema/collection_time)
Alias: collection_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  yes  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSamplingActivity](AerosolSamplingActivity.md), [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md), [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md), [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md), [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md), [PlantSamplingActivity](PlantSamplingActivity.md), [PureCultureSamplingActivity](PureCultureSamplingActivity.md), [SedimentSamplingActivity](SedimentSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md), [TerraformSamplingActivity](TerraformSamplingActivity.md), [WaterSamplingActivity](WaterSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:collection_time |
| native | analysis_api_schema:collection_time |




## LinkML Source

<details>
```yaml
name: collection_time
description: 'The time of sampling as an instance (single point). Required format:
  HH:MM:SS in 24-hour time format. Don''t forget the second! (Unit: hh:mm:ss or HH:MM:SS)'
title: collection time
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: collection_time
domain_of:
- AerosolSamplingActivity
- CultureEnvironmentalSamplingActivity
- FieldDeployedTerraformSamplingActivity
- MixedCultureSamplingActivity
- MonetSoilSamplingActivity
- OtherUndescribedSamplingActivity
- PlantSamplingActivity
- PureCultureSamplingActivity
- SedimentSamplingActivity
- SoilSamplingActivity
- TerraformSamplingActivity
- WaterSamplingActivity
range: string
pattern: ^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])\s*(hh:mm:ss|HH:MM:SS)$

```
</details>