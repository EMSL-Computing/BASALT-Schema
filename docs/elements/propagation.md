

# Slot: propagation (propagation) 


_The type of reproduction from the parent stock. Values for this field are specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual'_





URI: [basalt_schema:propagation](https://emsl-computing.github.io/BASALT-Schema/elements/propagation)
Alias: propagation

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:propagation |
| native | basalt_schema:propagation |




## LinkML Source

<details>
```yaml
name: propagation
description: 'The type of reproduction from the parent stock. Values for this field
  are specific to different taxa. For phage or virus: lytic/lysogenic/temperate/obligately
  lytic. For plasmids: incompatibility group. For eukaryotes: sexual/asexual'''
title: propagation
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: propagation
domain_of:
- organism
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
range: string

```
</details>