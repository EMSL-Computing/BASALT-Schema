

# Slot: raw_fasta_url 


_URL of raw FASTA file, if available from provider_





URI: [basalt_schema:raw_fasta_url](https://EMSL-Computing.github.io/basalt-schema/raw_fasta_url)
Alias: raw_fasta_url

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MetagenomicsProduct](MetagenomicsProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:raw_fasta_url |
| native | basalt_schema:raw_fasta_url |




## LinkML Source

<details>
```yaml
name: raw_fasta_url
description: URL of raw FASTA file, if available from provider
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: raw_fasta_url
domain_of:
- MetagenomicsProduct
range: string

```
</details>