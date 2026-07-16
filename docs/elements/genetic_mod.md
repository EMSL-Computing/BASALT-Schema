

# Slot: genetic modifications (genetic_mod) 


_Genetic modifications of the genome of an organism, which may occur naturally by spontaneous mutation or be introduced by some experimental means, e.g. specification of a transgene or the gene knocked-out or details of transient transfection_





URI: [analysis_api_schema:genetic_mod](https://w3id.org/MONet/analysis-api-schema/genetic_mod)
Alias: genetic_mod

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [SynthesizedMaterialSample](SynthesizedMaterialSample.md) | A sample containing synthetically generated material |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [PureCultureSample](PureCultureSample.md), [SynthesizedMaterialSample](SynthesizedMaterialSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:genetic_mod |
| native | analysis_api_schema:genetic_mod |




## LinkML Source

<details>
```yaml
name: genetic_mod
description: Genetic modifications of the genome of an organism, which may occur naturally
  by spontaneous mutation or be introduced by some experimental means, e.g. specification
  of a transgene or the gene knocked-out or details of transient transfection
title: genetic modifications
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: genetic_mod
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PlantSample
- PureCultureSample
- SynthesizedMaterialSample
- TerraformSample
range: string

```
</details>