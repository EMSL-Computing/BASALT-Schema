

# Slot: provider_name 


_Provider class (e.g., JGI, SeqCenter) using ontology terms where possible_





URI: [basalt_schema:provider_name](https://emsl-computing.github.io/BASALT-Schema/elements/provider_name)
Alias: provider_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |






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


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:provider_name |
| native | basalt_schema:provider_name |




## LinkML Source

<details>
```yaml
name: provider_name
description: Provider class (e.g., JGI, SeqCenter) using ontology terms where possible
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: provider_name
domain_of:
- MetagenomicsProduct
range: ControlledTermValue

```
</details>