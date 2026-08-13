

# Slot: sample_link 


_'A unique identifier to assign parent-child subsample or sibling samples. This is relevant when a sample or other material was used to generate the new sample. This field allows multiple entries separated by ; (Examples: Soil collected from the field will link with the soil used in an incubation. The soil a plant was grown in links to the plant sample. An original culture sample was transferred to a new vial and generated a new sample)'_





URI: [basalt_schema:sample_link](https://EMSL-Computing.github.io/basalt-schema/sample_link)
Alias: sample_link

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [AerosolSample](AerosolSample.md) | An aerosol sample collected from the environment |  no  |
| [AerosolArmSample](AerosolArmSample.md) | An aerosol sample collected by the ARM facility |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AerosolArmSample](AerosolArmSample.md), [AerosolSample](AerosolSample.md), [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |








## TODOs

* EMSL and NMDC both need better modelling for this



## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:sample_link |
| native | basalt_schema:sample_link |




## LinkML Source

<details>
```yaml
name: sample_link
description: '''A unique identifier to assign parent-child subsample or sibling samples.
  This is relevant when a sample or other material was used to generate the new sample.
  This field allows multiple entries separated by ; (Examples: Soil collected from
  the field will link with the soil used in an incubation. The soil a plant was grown
  in links to the plant sample. An original culture sample was transferred to a new
  vial and generated a new sample)'''
todos:
- EMSL and NMDC both need better modelling for this
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: sample_link
domain_of:
- AerosolArmSample
- AerosolSample
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