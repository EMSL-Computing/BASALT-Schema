

# Slot: emsl_activity 


_Nullable string linking a Sample or SamplingActivity to a named EMSL activity or_

_campaign (e.g., 'AMP2', 'MONet_FY26'). Optional for historical records_

_predating activity tracking._





URI: [basalt_schema:emsl_activity](https://EMSL-Computing.github.io/basalt-schema/emsl_activity)
Alias: emsl_activity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [AerosolSamplingActivity](AerosolSamplingActivity.md) | A sampling activity where aerosol samples were collected |  no  |
| [OtherUndescribedSamplingActivity](OtherUndescribedSamplingActivity.md) | Collection of samples from source that does not fit into any of the other cat... |  no  |
| [PlantSamplingActivity](PlantSamplingActivity.md) | Collection of samples associated with plants |  no  |
| [PureCultureSamplingActivity](PureCultureSamplingActivity.md) | Collection of samples from a culture containing a single organism |  no  |
| [WaterSamplingActivity](WaterSamplingActivity.md) | Collection of water samples |  no  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [Sample](Sample.md) | A physical sample collected from an environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSamplingActivity](SoilSamplingActivity.md) | Collection of soil samples from the environment |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [MonetSoilSamplingActivity](MonetSoilSamplingActivity.md) | Collection of soil cores according to the MONet soil sampling protocol |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [AerosolArmSamplingActivity](AerosolArmSamplingActivity.md) | A sampling activity where aerosol samples were collected by ARM |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |
| [SedimentSamplingActivity](SedimentSamplingActivity.md) | Collection of sediment samples from the environment |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [TerraformSamplingActivity](TerraformSamplingActivity.md) | Collection of samples from a Terraform device |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [CommerciallyPurchasedSamplingActivity](CommerciallyPurchasedSamplingActivity.md) | Collection of samples that were purchased by the user |  no  |
| [MixedCultureSamplingActivity](MixedCultureSamplingActivity.md) | Collection of samples from a mixed culture |  no  |
| [SynthesizedMaterialSamplingActivity](SynthesizedMaterialSamplingActivity.md) | Collection of samples of a synthesized material |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [SamplingActivity](SamplingActivity.md) | An activity that involves the collection of a sample |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |
| [FieldDeployedTerraformSamplingActivity](FieldDeployedTerraformSamplingActivity.md) | Collection of samples from a field-deployed Terraform device |  no  |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [CultureEnvironmentalSamplingActivity](CultureEnvironmentalSamplingActivity.md) | Collection of samples from a culture of organisms taken from the environment |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [EngineeredStrainSamplingActivity](EngineeredStrainSamplingActivity.md) | Collection of samples from a culture of an engineered organism |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Sample](Sample.md), [SamplingActivity](SamplingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* Is sampling activity where we want to capture this?



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:emsl_activity |
| native | basalt_schema:emsl_activity |




## LinkML Source

<details>
```yaml
name: emsl_activity
description: 'Nullable string linking a Sample or SamplingActivity to a named EMSL
  activity or

  campaign (e.g., ''AMP2'', ''MONet_FY26''). Optional for historical records

  predating activity tracking.'
todos:
- Is sampling activity where we want to capture this?
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: emsl_activity
domain_of:
- Sample
- SamplingActivity
range: string
required: false

```
</details>