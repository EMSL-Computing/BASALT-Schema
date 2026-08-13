

# Slot: host taxonomy identifier (host_taxid) 


_NCBI taxon ID. Format with prefix NCBITaxon:####_





URI: [basalt_schema:host_taxid](https://EMSL-Computing.github.io/BASALT-Schema/host_taxid)
Alias: host_taxid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [Organism](Organism.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |






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









## Aliases


* host_taxonomy_id
* host_ncbi_taxon_id
* host_taxa_id




## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:host_taxid |
| native | basalt_schema:host_taxid |




## LinkML Source

<details>
```yaml
name: host_taxid
description: NCBI taxon ID. Format with prefix NCBITaxon:####
title: host taxonomy identifier
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
aliases:
- host_taxonomy_id
- host_ncbi_taxon_id
- host_taxa_id
rank: 1000
alias: host_taxid
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