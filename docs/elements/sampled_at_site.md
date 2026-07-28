

# Slot: sampled_at_site 


_Reference to the site where the sample was collected. This is a FK to the Site class, which contains detailed metadata about the sampling location._





URI: [analysis_api_schema:sampled_at_site](https://w3id.org/MONet/analysis-api-schema/sampled_at_site)
Alias: sampled_at_site

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [AerosolArmSamplingActivity](AerosolArmSamplingActivity.md) | A sampling activity where aerosol samples were collected by ARM |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [SamplingActivity](SamplingActivity.md) | An activity that involves the collection of a sample |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [EngineeredStrainSamplingActivity](EngineeredStrainSamplingActivity.md) | Collection of samples from a culture of an engineered organism |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:sampled_at_site |
| native | analysis_api_schema:sampled_at_site |




## LinkML Source

<details>
```yaml
name: sampled_at_site
description: Reference to the site where the sample was collected. This is a FK to
  the Site class, which contains detailed metadata about the sampling location.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: sampled_at_site
domain_of:
- SamplingActivity
range: Site

```
</details>