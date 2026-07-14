

# Slot: host taxonomy identifier (host_taxid) 


_NCBI taxon ID. Format with prefix NCBITaxon:####_





URI: [analysis_api_schema:host_taxid](https://w3id.org/MONet/analysis-api-schema/host_taxid)
Alias: host_taxid

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TerraformSample](TerraformSample.md) | A sample collected from a Terraform experiment |  no  |
| [BiologicalEntity](BiologicalEntity.md) | Reference data representing a biological identity (strain, isolate, |  no  |
| [MixedCultureSample](MixedCultureSample.md) | A sample containing multiple cultured organisms |  yes  |
| [PureCultureSample](PureCultureSample.md) | A sample of a culture containing a single organism |  yes  |
| [CultureEnvironmentalSample](CultureEnvironmentalSample.md) | A sample containing organisms cultured from an environmental sample |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [FieldDeployedTerraformSample](FieldDeployedTerraformSample.md) | A sample collected from a field-deployed Terraform experiment |  no  |







## Properties

* Range: [String](String.md)

* Regex pattern: `NCBITaxon:\d+`



## Aliases


* host_taxonomy_id
* host_ncbi_taxon_id
* host_taxa_id



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:host_taxid |
| native | analysis_api_schema:host_taxid |




## LinkML Source

<details>
```yaml
name: host_taxid
description: NCBI taxon ID. Format with prefix NCBITaxon:####
title: host taxonomy identifier
from_schema: https://w3id.org/MONet/analysis-api-schema
aliases:
- host_taxonomy_id
- host_ncbi_taxon_id
- host_taxa_id
rank: 1000
alias: host_taxid
domain_of:
- CultureEnvironmentalSample
- FieldDeployedTerraformSample
- MixedCultureSample
- OtherUndescribedSample
- PureCultureSample
- TerraformSample
- biological_entity
range: string
pattern: NCBITaxon:\d+

```
</details>