

# Slot: oxygen relationship (oxygen_relationship) 


_The relationship of the sample to oxygen, such as aerobic or anaerobic._





URI: [basalt_schema:oxygen_relationship](https://w3id.org/MONet/basalt-schema/oxygen_relationship)
Alias: oxygen_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [EcoplatePlateSetupActivity](EcoplatePlateSetupActivity.md) | Ecoplate-specific plate setup |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [AMP2PlateSetupActivity](AMP2PlateSetupActivity.md) | AMP2-specific plate setup |  no  |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [HasIncubationConditions](HasIncubationConditions.md) | Mixin for activities/setups that involve controlled incubation |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlateSetupActivity](PlateSetupActivity.md) | Abstract base for 96-well plate setup activities |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OxygenStatusEnum](OxygenStatusEnum.md) |
| Domain Of | [HasIncubationConditions](HasIncubationConditions.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:oxygen_relationship |
| native | basalt_schema:oxygen_relationship |
| exact | MIXS:0000015 |




## LinkML Source

<details>
```yaml
name: oxygen_relationship
description: The relationship of the sample to oxygen, such as aerobic or anaerobic.
title: oxygen relationship
from_schema: https://w3id.org/MONet/basalt-schema
exact_mappings:
- MIXS:0000015
rank: 1000
alias: oxygen_status
domain_of:
- HasIncubationConditions
- CommerciallyPurchasedSample
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- TerraformSample
- WaterSample
range: OxygenStatusEnum

```
</details>