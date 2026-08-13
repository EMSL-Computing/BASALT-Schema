# Enum: AnalyteCategoryEnum 




_bundling common terms for different omics types by biomolecule being analyzed_



URI: [basalt_schema:AnalyteCategoryEnum](https://EMSL-Computing.github.io/BASALT-Schema/AnalyteCategoryEnum)

## Permissible Values
| Value | Meaning | Description |
| --- | --- | --- |
| dna | None |  |
| rna | None |  |
| protein | None |  |
| metabolite | None |  |
| lipid | None |  |
| natural_organic_matter | None |  |
| unknown | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [analyte_category](analyte_category.md) | omics type for easier search, optional |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: AnalyteCategoryEnum
description: bundling common terms for different omics types by biomolecule being
  analyzed
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  dna:
    text: dna
    aliases:
    - genome
    - genomics
    - metagenome
    - metagenomics
    - metaG
  rna:
    text: rna
    aliases:
    - transcriptome
    - transcriptomics
    - metatranscriptome
    - metatranscriptomics
    - metaT
  protein:
    text: protein
    aliases:
    - proteins
    - proteome
    - proteomics
    - metaproteome
    - metaproteomics
    - metaP
  metabolite:
    text: metabolite
    aliases:
    - metabolites
    - metabolome
    - metabolomics
  lipid:
    text: lipid
    aliases:
    - lipids
    - lipidome
    - lipidomics
  natural_organic_matter:
    text: natural_organic_matter
    aliases:
    - NOM
  unknown:
    text: unknown

```
</details>