

# Slot: analysis_type 


_The type(s) of analysis planned for this sample._





URI: [basalt_schema:analysis_type](https://emsl-computing.github.io/BASALT-Schema/elements/analysis_type)
Alias: analysis_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  yes  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  yes  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  yes  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  yes  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  yes  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [AMP2UserSample](AMP2UserSample.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




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
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: analysis_type
domain_of:
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