

# Slot: analysis_type 


_The type(s) of analysis planned for this sample._





URI: [basalt_schema:analysis_type](https://EMSL-Computing.github.io/basalt-schema/analysis_type)
Alias: analysis_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  yes  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [SampleProcessing](SampleProcessing.md) | Abstract base for any sample processing activity (physical to physical) |  no  |
| [MediaPreparation](MediaPreparation.md) | Activity that prepares a batch of growth media |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SampleProcessing](SampleProcessing.md), [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [AMP2UserSample](AMP2UserSample.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:analysis_type |
| native | basalt_schema:analysis_type |




## LinkML Source

<details>
```yaml
name: analysis_type
description: The type(s) of analysis planned for this sample.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: analysis_type
domain_of:
- SampleProcessing
- AerosolArmSample
- AerosolSample
- AMP2UserSample
- CommerciallyPurchasedSample
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- TerraformSample
- WaterSample
range: string

```
</details>