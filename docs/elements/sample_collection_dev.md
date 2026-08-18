

# Slot: sample collection device (sample_collection_dev) 


_The device used to collect an environmental sample. Include dimensions of device if applicable_





URI: [basalt_schema:sample_collection_dev](https://emsl-computing.github.io/BASALT-Schema/elements/sample_collection_dev)
Alias: sample_collection_dev

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  yes  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  yes  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolSamplingActivity](AerosolSamplingActivity.md), [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md), [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md), [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md), [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md), [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md), [PlantSamplingActivity](PlantSamplingActivity.md), [PureCultureSamplingActivity](PureCultureSamplingActivity.md), [SedimentSamplingActivity](SedimentSamplingActivity.md), [SoilSamplingActivity](SoilSamplingActivity.md), [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md), [WaterSamplingActivity](WaterSamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_collection_dev |
| native | basalt_schema:sample_collection_dev |




## LinkML Source

<details>
```yaml
name: sample_collection_dev
description: The device used to collect an environmental sample. Include dimensions
  of device if applicable
title: sample collection device
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sample_collection_dev
domain_of:
- AerosolSamplingActivity
- CommerciallyPurchasedSamplingActivity
- CultureEnvironmentalSamplingActivity
- MixedCultureSamplingActivity
- MonetSoilSamplingActivity
- OtherUndescribedSamplingActivity
- PlantSamplingActivity
- PureCultureSamplingActivity
- SedimentSamplingActivity
- SoilSamplingActivity
- SynthesizedMaterialSamplingActivity
- WaterSamplingActivity
range: string

```
</details>