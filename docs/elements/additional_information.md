

# Slot: additional_information 


_Additional information pertaining to these data, including SP Project ID and Taxon OID_





URI: [basalt_schema:additional_information](https://EMSL-Computing.github.io/basalt-schema/additional_information)
Alias: additional_information

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |






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
| self | basalt_schema:additional_information |
| native | basalt_schema:additional_information |




## LinkML Source

<details>
```yaml
name: additional_information
description: Additional information pertaining to these data, including SP Project
  ID and Taxon OID
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: additional_information
domain_of:
- MetagenomicsProduct
range: string

```
</details>