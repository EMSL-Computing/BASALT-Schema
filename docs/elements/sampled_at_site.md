

# Slot: sampled_at_site 


_Reference to the site where the sample was collected. This is a FK to the Site class, which contains detailed metadata about the sampling location._





URI: [basalt_schema:sampled_at_site](https://emsl-computing.github.io/BASALT-Schema/elements/sampled_at_site)
Alias: sampled_at_site

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [SamplingActivity](SamplingActivity.md) | An activity that involves the collection of a sample |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [EngineeredStrainSamplingActivity](EngineeredStrainSamplingActivity.md) | Collection of samples from a culture of an engineered organism |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [AerosolArmSamplingActivity](AerosolArmSamplingActivity.md) | A sampling activity where aerosol samples were collected by ARM |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Site](Site.md) |
| Domain Of | [SamplingActivity](SamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sampled_at_site |
| native | basalt_schema:sampled_at_site |




## LinkML Source

<details>
```yaml
name: sampled_at_site
description: Reference to the site where the sample was collected. This is a FK to
  the Site class, which contains detailed metadata about the sampling location.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: sampled_at_site
domain_of:
- SamplingActivity
range: Site

```
</details>