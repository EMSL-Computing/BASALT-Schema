

# Slot: observed biotic relationship (biotic_relationship) 


_Description of relationship(s) between the subject organism and other organism(s) it is associated with. E.g. parasite on species X; mutualist with species Y. The target organism is the subject of the relationship and the other organism(s) is the object_





URI: [basalt_schema:biotic_relationship](https://EMSL-Computing.github.io/BASALT-Schema/biotic_relationship)
Alias: biotic_relationship

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  yes  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BioticRelationshipEnum](BioticRelationshipEnum.md) |
| Domain Of | [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* samp_biotic_relationship




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:biotic_relationship |
| native | basalt_schema:biotic_relationship |
| exact | MIXS:0000016 |




## LinkML Source

<details>
```yaml
name: biotic_relationship
description: Description of relationship(s) between the subject organism and other
  organism(s) it is associated with. E.g. parasite on species X; mutualist with species
  Y. The target organism is the subject of the relationship and the other organism(s)
  is the object
title: observed biotic relationship
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
aliases:
- samp_biotic_relationship
exact_mappings:
- MIXS:0000016
rank: 1000
alias: biotic_relationship
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- SedimentSample
- SoilSample
- TerraformSample
range: BioticRelationshipEnum

```
</details>