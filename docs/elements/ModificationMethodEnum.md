# Enum: ModificationMethodEnum 




_Methods used to introduce genetic modifications into organisms._



URI: [basalt_schema:ModificationMethodEnum](https://EMSL-Computing.github.io/basalt-schema/ModificationMethodEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| electroporation | None | Introduction of DNA via electrical pulses ||
| conjugation | None | Transfer of DNA via bacterial conjugation ||
| transformation | None | Natural or chemical competence-based DNA uptake ||
| transduction | None | Phage-mediated DNA transfer ||
| crispr | None | CRISPR-based genome editing ||
| homologous_recombination | None | Integration via homologous recombination ||
| transposon | None | Transposon-mediated insertion ||
| other | None | Other modification method not listed | Title: Other<br>|
| p_element | None |  | Title: P-element<br>|
| phage_transformation | None |  | Title: Phage Transformation<br>|
| piggybac | None |  | Title: Piggybac<br>|
| polyethylene_glycol_mediated | None |  | Title: Polyethylene Glycol-mediated<br>|
| replicon | None |  | Title: Replicon<br>|
| whisker_mediated_transformation | None |  | Title: Whisker-mediated Transformation<br>|




## Slots

| Name | Description |
| ---  | --- |
| [modification_method](modification_method.md) | Select the method used to insert your construct into the genome of |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema






## LinkML Source

<details>
```yaml
name: ModificationMethodEnum
description: Methods used to introduce genetic modifications into organisms.
from_schema: https://EMSL-Computing.github.io/basalt-schema
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
    title: Other
  p_element:
    text: p_element
    title: P-element
  phage_transformation:
    text: phage_transformation
    title: Phage Transformation
  piggybac:
    text: piggybac
    title: Piggybac
  polyethylene_glycol_mediated:
    text: polyethylene_glycol_mediated
    title: Polyethylene Glycol-mediated
  replicon:
    text: replicon
    title: Replicon
  whisker_mediated_transformation:
    text: whisker_mediated_transformation
    title: Whisker-mediated Transformation

```
</details>