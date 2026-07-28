

# Slot: mg_workflow_step 


_Metagenomics workflow step that produced this product (e.g., MagsAnalysis)_





URI: [analysis_api_schema:mg_workflow_step](https://w3id.org/MONet/analysis-api-schema/mg_workflow_step)
Alias: mg_workflow_step

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MetagenomicsBinningProduct](MetagenomicsBinningProduct.md) | Top-level archive (zip/tar) for binning results stored in MinIO |  no  |
| [MetagenomicsAnnotationProduct](MetagenomicsAnnotationProduct.md) | Top-level archive for functional annotation outputs (zip/tar stored in MinIO) |  no  |
| [MetagenomicsProduct](MetagenomicsProduct.md) | Abstract base for all metagenomics data products |  no  |
| [MetagenomicsGenePhylogenyProduct](MetagenomicsGenePhylogenyProduct.md) | Top-level archive for gene-based phylogeny outputs (zip/tar stored in MinIO) |  no  |






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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:mg_workflow_step |
| native | analysis_api_schema:mg_workflow_step |




## LinkML Source

<details>
```yaml
name: mg_workflow_step
description: Metagenomics workflow step that produced this product (e.g., MagsAnalysis)
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: mg_workflow_step
domain_of:
- MetagenomicsProduct
range: MetagenomicsSteps
required: false

```
</details>