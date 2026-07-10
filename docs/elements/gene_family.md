

# Slot: gene_family 


_Gene family or marker used for the phylogeny (e.g., 16S, ITS)_





URI: [analysis_api_schema:gene_family](https://w3id.org/MONet/analysis-api-schema/gene_family)
Alias: gene_family

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:gene_family |
| native | analysis_api_schema:gene_family |




## LinkML Source

<details>
```yaml
name: gene_family
description: Gene family or marker used for the phylogeny (e.g., 16S, ITS)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: gene_family
domain_of:
- Metagenomics_GenePhylogenyProduct
range: string
required: false

```
</details>