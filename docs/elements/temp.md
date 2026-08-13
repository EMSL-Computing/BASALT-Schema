

# Slot: temperature (temp) 


_Temperature of the sample at the time of sampling. (Units: C)_





URI: [basalt_schema:temp](https://EMSL-Computing.github.io/basalt-schema/temp)
Alias: temp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [MonetSoilSample](MonetSoilSample.md) | A soil sample that has been collected according to the MONet soil sampling pr... |  yes  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md) | A sample containing commercially purchased material |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CommerciallyPurchasedSample](CommerciallyPurchasedSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MonetSoilSample](MonetSoilSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^-?\d+(\.\d+)?\s*C$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:temp |
| native | basalt_schema:temp |




## LinkML Source

<details>
```yaml
name: temp
description: 'Temperature of the sample at the time of sampling. (Units: C)'
title: temperature
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: temp
domain_of:
- CommerciallyPurchasedSample
- FieldDeployedTerraformSample
- MonetSoilSample
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- SynthesizedMaterialSample
- TerraformSample
- WaterSample
range: string
pattern: ^-?\d+(\.\d+)?\s*C$

```
</details>