

# Slot: host specificity or range (host_spec_range) 


_The range and diversity of host species that an organism is capable of infecting, defined by NCBI taxonomy identifier. Format with prefix NCBITaxon:####_





URI: [basalt_schema:host_spec_range](https://emsl-computing.github.io/BASALT-Schema/elements/host_spec_range)
Alias: host_spec_range

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  no  |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Organism](Organism.md), [CultureEnvironmentalSample](CultureEnvironmentalSample.md), [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md), [MixedCultureSample](MixedCultureSample.md), [OtherUndescribedSample](OtherUndescribedSample.md), [PureCultureSample](PureCultureSample.md), [TerraformSample](TerraformSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `NCBITaxon:\d+` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_spec_range |
| native | basalt_schema:host_spec_range |




## LinkML Source

<details>
```yaml
name: host_spec_range
description: The range and diversity of host species that an organism is capable of
  infecting, defined by NCBI taxonomy identifier. Format with prefix NCBITaxon:####
title: host specificity or range
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: host_spec_range
domain_of:
- organism
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
range: string
pattern: NCBITaxon:\d+

```
</details>