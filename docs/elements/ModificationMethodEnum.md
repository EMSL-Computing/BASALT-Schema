# Enum: ModificationMethodEnum 




_Methods used to introduce genetic modifications into organisms._



URI: [ModificationMethodEnum](ModificationMethodEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| electroporation | None | Introduction of DNA via electrical pulses |
| conjugation | None | Transfer of DNA via bacterial conjugation |
| transformation | None | Natural or chemical competence-based DNA uptake |
| transduction | None | Phage-mediated DNA transfer |
| crispr | None | CRISPR-based genome editing |
| homologous_recombination | None | Integration via homologous recombination |
| transposon | None | Transposon-mediated insertion |
| other | None | Other modification method not listed |




## Slots

| Name | Description |
| ---  | --- |
| [modification_method](modification_method.md) | Select the method used to insert your construct into the genome of |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema






## LinkML Source

<details>
```yaml
name: ModificationMethodEnum
description: Methods used to introduce genetic modifications into organisms.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
permissible_values:
  electroporation:
    text: electroporation
    description: Introduction of DNA via electrical pulses
    aliases:
    - Electroporation
  conjugation:
    text: conjugation
    description: Transfer of DNA via bacterial conjugation
    aliases:
    - Conjugation
  transformation:
    text: transformation
    description: Natural or chemical competence-based DNA uptake
    aliases:
    - Transformation
  transduction:
    text: transduction
    description: Phage-mediated DNA transfer
    aliases:
    - Transduction
  crispr:
    text: crispr
    description: CRISPR-based genome editing
    aliases:
    - CRISPR
    - CRISPR-Cas
  homologous_recombination:
    text: homologous_recombination
    description: Integration via homologous recombination
  transposon:
    text: transposon
    description: Transposon-mediated insertion
  other:
    text: other
    description: Other modification method not listed

```
</details>
