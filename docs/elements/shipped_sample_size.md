

# Slot: shipped sample size (shipped_sample_size) 


_Total amount of sample sent to EMSL. Must include units._





URI: [basalt_schema:shipped_sample_size](https://w3id.org/MONet/basalt-schema/shipped_sample_size)
Alias: shipped_sample_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [AerosolArmSamplingActivity](AerosolArmSamplingActivity.md) | A sampling activity where aerosol samples were collected by ARM |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [SamplingActivity](SamplingActivity.md) | An activity that involves the collection of a sample |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [EngineeredStrainSamplingActivity](EngineeredStrainSamplingActivity.md) | Collection of samples from a culture of an engineered organism |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2UserSample](AMP2UserSample.md), [SamplingActivity](SamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*[\w\s/]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:shipped_sample_size |
| native | basalt_schema:shipped_sample_size |




## LinkML Source

<details>
```yaml
name: shipped_sample_size
description: Total amount of sample sent to EMSL. Must include units.
title: shipped sample size
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: shipped_sample_size
domain_of:
- AMP2UserSample
- SamplingActivity
range: string
pattern: ^\d+(\.\d+)?\s*[\w\s/]+$

```
</details>