

# Slot: sample collected (sample_collected) 


_This refers to the TOTAL amount of sample collected from the experiment. NOT the amount sent to EMSL or collected for a specific analysis. Provide value and unit, any unit is valid_





URI: [basalt_schema:sample_collected](https://EMSL-Computing.github.io/BASALT-Schema/sample_collected)
Alias: sample_collected

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSamplingActivity](AerosolSamplingActivity.md), [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md), [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md), [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md), [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md), [PlantSamplingActivity](PlantSamplingActivity.md), [PureCultureSamplingActivity](PureCultureSamplingActivity.md), [SedimentSamplingActivity](SedimentSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md), [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md), [TerraformSamplingActivity](TerraformSamplingActivity.md), [WaterSamplingActivity](WaterSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_collected |
| native | basalt_schema:sample_collected |




## LinkML Source

<details>
```yaml
name: sample_collected
description: This refers to the TOTAL amount of sample collected from the experiment.
  NOT the amount sent to EMSL or collected for a specific analysis. Provide value
  and unit, any unit is valid
title: sample collected
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: sample_collected
domain_of:
- AerosolSamplingActivity
- CommerciallyPurchasedSamplingActivity
- CultureEnvironmentalSamplingActivity
- FieldDeployedTerraformSamplingActivity
- MixedCultureSamplingActivity
- OtherUndescribedSamplingActivity
- PlantSamplingActivity
- PureCultureSamplingActivity
- SedimentSamplingActivity
- SoilSamplingActivity
- SynthesizedMaterialSamplingActivity
- TerraformSamplingActivity
- WaterSamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>