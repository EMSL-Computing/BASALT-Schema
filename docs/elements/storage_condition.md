

# Slot: storage condition (storage_condition) 


_The storage condition of the sample. This field is NOT multivalued. If selecting other add the `other_storage_condt` attribute to provide additional detail._





URI: [analysis_api_schema:storage_condition](https://w3id.org/MONet/analysis-api-schema/storage_condition)
Alias: storage_condition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  yes  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [EngineeredStrainSample](EngineeredStrainSample.md) | A sample containing a strain of an organism that has been subjected to geneti... |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StorageConditionEnum](StorageConditionEnum.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [AMP2UserSample](AMP2UserSample.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [EngineeredStrainSample](EngineeredStrainSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* samp_store_cond
* storage_cond
* storage_condt




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:storage_condition |
| native | analysis_api_schema:storage_condition |
| exact | MIXS:0000327 |




## LinkML Source

<details>
```yaml
name: storage_condition
description: The storage condition of the sample. This field is NOT multivalued. If
  selecting other add the `other_storage_condt` attribute to provide additional detail.
title: storage condition
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- samp_store_cond
- storage_cond
- storage_condt
exact_mappings:
- MIXS:0000327
rank: 1000
alias: storage_condition
domain_of:
- AerosolArmSample
- AerosolSample
- AMP2UserSample
- CommerciallyPurchasedSample
- CultureEnvironmentalSample
- EngineeredStrainSample
- FieldDeployedTerraformSample
- MixedCultureSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- TerraformSample
- WaterSample
range: StorageConditionEnum

```
</details>