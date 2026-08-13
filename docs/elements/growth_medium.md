

# Slot: growth medium (growth_medium) 


_Method of growth and medium/materials used. Indicate broth, gel, 3-D structure, bioreactor, etc. followed by the formula, recipe, or components used to create the growth medium._





URI: [basalt_schema:growth_medium](https://EMSL-Computing.github.io/BASALT-Schema/growth_medium)
Alias: growth_medium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PreCultureGrowth](PreCultureGrowth.md) | Growth of a pre-culture to establish viable inoculum before |  no  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [ExperimentalCulture](ExperimentalCulture.md) | Growth of an experimental culture for downstream analysis |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [CultureGrowth](CultureGrowth.md) | Abstract activity for growing cultures from samples or other cultures |  no  |
| [StockCulturePreparation](StockCulturePreparation.md) | Preparation of a stock culture from user samples for long-term storage |  no  |
| [StrainPurity](StrainPurity.md) | Purity check of a strain culture |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CultureGrowth](CultureGrowth.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:growth_medium |
| native | basalt_schema:growth_medium |




## LinkML Source

<details>
```yaml
name: growth_medium
description: Method of growth and medium/materials used. Indicate broth, gel, 3-D
  structure, bioreactor, etc. followed by the formula, recipe, or components used
  to create the growth medium.
title: growth medium
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: growth_medium
domain_of:
- CultureGrowth
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
range: string

```
</details>