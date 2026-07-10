

# Slot: raw_fasta_url 


_URL of raw FASTA file, if available from provider_





URI: [analysis_api_schema:raw_fasta_url](https://w3id.org/MONet/analysis-api-schema/raw_fasta_url)
Alias: raw_fasta_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:raw_fasta_url |
| native | analysis_api_schema:raw_fasta_url |




## LinkML Source

<details>
```yaml
name: raw_fasta_url
description: URL of raw FASTA file, if available from provider
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: raw_fasta_url
domain_of:
- MetagenomicsProduct
range: string

```
</details>