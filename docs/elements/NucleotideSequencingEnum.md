# Enum: NucleotideSequencingEnum 



URI: [basalt_schema:NucleotideSequencingEnum](https://emsl-computing.github.io/BASALT-Schema/elements/NucleotideSequencingEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| metagenome | None |  | Title: Metagenome<br>|
| metatranscriptome | None |  | Title: Metatranscriptome<br>|
| amplicon_sequencing_assay | OBI:0002767 |  | Title: Amplicon<br>|




## Slots

| Name | Description |
| ---  | --- |
| [nucleotide_sequencing_category](nucleotide_sequencing_category.md) | The category of nucleotide sequencing performed (e |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: NucleotideSequencingEnum
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  metagenome:
    text: metagenome
    title: Metagenome
    aliases:
    - metaG
  metatranscriptome:
    text: metatranscriptome
    title: Metatranscriptome
    aliases:
    - metaT
  amplicon_sequencing_assay:
    text: amplicon_sequencing_assay
    meaning: OBI:0002767
    title: Amplicon

```
</details>