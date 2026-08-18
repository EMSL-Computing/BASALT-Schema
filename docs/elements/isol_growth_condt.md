

# Slot: isolation and growth conditions (isol_growth_condt) 


_Publication reference in the form of pubmed ID (PMID), digital object_

_identifier (DOI), or URL for isolation and growth condition specifications of the_

_organism/material_





URI: [basalt_schema:isol_growth_condt](https://EMSL-Computing.github.io/BASALT-Schema/isol_growth_condt)
Alias: isol_growth_condt

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [AMP2UserSample](AMP2UserSample.md) | A user-submitted microbial sample for AMP2 workflows |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AMP2UserSample](AMP2UserSample.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:isol_growth_condt |
| native | basalt_schema:isol_growth_condt |




## LinkML Source

<details>
```yaml
name: isol_growth_condt
description: 'Publication reference in the form of pubmed ID (PMID), digital object

  identifier (DOI), or URL for isolation and growth condition specifications of the

  organism/material'
title: isolation and growth conditions
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: isol_growth_condt
domain_of:
- AMP2UserSample
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
range: string

```
</details>