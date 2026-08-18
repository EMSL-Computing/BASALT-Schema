

# Slot: host common name (host_common_name) 


_Common name for the host organism (e.g., "Pseudomonas putida")._

_For microbes, this may be identical to organism_name._





URI: [basalt_schema:host_common_name](https://emsl-computing.github.io/BASALT-Schema/elements/host_common_name)
Alias: host_common_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
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







## Aliases


* common_name




## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_common_name |
| native | basalt_schema:host_common_name |




## LinkML Source

<details>
```yaml
name: host_common_name
description: 'Common name for the host organism (e.g., "Pseudomonas putida").

  For microbes, this may be identical to organism_name.'
title: host common name
from_schema: https://emsl-computing.github.io/BASALT-Schema
aliases:
- common_name
rank: 1000
alias: host_common_name
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