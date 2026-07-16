

# Slot: sample collection method (sample_collection_method) 


_The method used to collect an environmental sample. This can be a citation or description._





URI: [analysis_api_schema:sample_collection_method](https://w3id.org/MONet/analysis-api-schema/sample_collection_method)
Alias: sample_collection_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  yes  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md), [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md), [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md), [PlantSamplingActivity](PlantSamplingActivity.md), [PureCultureSamplingActivity](PureCultureSamplingActivity.md), [SedimentSamplingActivity](SedimentSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md), [TerraformSamplingActivity](TerraformSamplingActivity.md), [WaterSamplingActivity](WaterSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sample_collection_method |
| native | analysis_api_schema:sample_collection_method |




## LinkML Source

<details>
```yaml
name: sample_collection_method
description: The method used to collect an environmental sample. This can be a citation
  or description.
title: sample collection method
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sample_collection_method
domain_of:
- CultureEnvironmentalSamplingActivity
- FieldDeployedTerraformSamplingActivity
- MixedCultureSamplingActivity
- OtherUndescribedSamplingActivity
- PlantSamplingActivity
- PureCultureSamplingActivity
- SedimentSamplingActivity
- SoilSamplingActivity
- TerraformSamplingActivity
- WaterSamplingActivity
range: string

```
</details>