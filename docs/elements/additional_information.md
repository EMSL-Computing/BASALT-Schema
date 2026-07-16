

# Slot: additional_information 


_Additional information pertaining to these data, including SP Project ID and Taxon OID_





URI: [analysis_api_schema:additional_information](https://w3id.org/MONet/analysis-api-schema/additional_information)
Alias: additional_information

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:additional_information |
| native | analysis_api_schema:additional_information |




## LinkML Source

<details>
```yaml
name: additional_information
description: Additional information pertaining to these data, including SP Project
  ID and Taxon OID
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: additional_information
domain_of:
- MetagenomicsProduct
range: string

```
</details>