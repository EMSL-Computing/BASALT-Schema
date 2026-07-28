

# Slot: provider_name 


_Provider class (e.g., JGI, SeqCenter) using ontology terms where possible_





URI: [analysis_api_schema:provider_name](https://w3id.org/MONet/analysis-api-schema/provider_name)
Alias: provider_name

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
| Range | [ControlledTermValue](ControlledTermValue.md) |
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
| self | analysis_api_schema:provider_name |
| native | analysis_api_schema:provider_name |




## LinkML Source

<details>
```yaml
name: provider_name
description: Provider class (e.g., JGI, SeqCenter) using ontology terms where possible
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: provider_name
domain_of:
- MetagenomicsProduct
range: ControlledTermValue

```
</details>