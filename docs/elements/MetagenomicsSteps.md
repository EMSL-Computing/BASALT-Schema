# Enum: MetagenomicsSteps 



URI: [basalt_schema:MetagenomicsSteps](https://EMSL-Computing.github.io/BASALT-Schema/MetagenomicsSteps)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| ReadQcAnalysis | None |  |
| MetagenomeAssembly | None |  |
| ReadBasedTaxonomyAnalysis | None |  |
| MetagenomeAnnotation | None |  |
| MagsAnalysis | None |  |
| FunctionalAnnotation | None |  |
| GenePhylogeny | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [mg_workflow_step](mg_workflow_step.md) | Metagenomics workflow step that produced this product (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: MetagenomicsSteps
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  ReadQcAnalysis:
    text: ReadQcAnalysis
  MetagenomeAssembly:
    text: MetagenomeAssembly
  ReadBasedTaxonomyAnalysis:
    text: ReadBasedTaxonomyAnalysis
  MetagenomeAnnotation:
    text: MetagenomeAnnotation
  MagsAnalysis:
    text: MagsAnalysis
  FunctionalAnnotation:
    text: FunctionalAnnotation
  GenePhylogeny:
    text: GenePhylogeny

```
</details>