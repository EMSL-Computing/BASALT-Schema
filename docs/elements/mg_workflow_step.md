

# Slot: mg_workflow_step 


_Metagenomics workflow step that produced this product (e.g., MagsAnalysis)_





URI: [basalt_schema:mg_workflow_step](https://EMSL-Computing.github.io/basalt-schema/mg_workflow_step)
Alias: mg_workflow_step

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MetagenomicsSteps](MetagenomicsSteps.md) |
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
| self | basalt_schema:mg_workflow_step |
| native | basalt_schema:mg_workflow_step |




## LinkML Source

<details>
```yaml
name: mg_workflow_step
description: Metagenomics workflow step that produced this product (e.g., MagsAnalysis)
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: mg_workflow_step
domain_of:
- MetagenomicsProduct
range: MetagenomicsSteps
required: false

```
</details>