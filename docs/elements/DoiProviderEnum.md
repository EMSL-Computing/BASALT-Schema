# Enum: DoiProviderEnum 




_The authority, or organization, the DOI is associated with_



URI: [basalt_schema:DoiProviderEnum](https://EMSL-Computing.github.io/BASALT-Schema/DoiProviderEnum)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| emsl | ror:04rc0xn13 |  | Title: EMSL<br>|
| jgi | ror:04xm1d337 |  | Title: JGI<br>|
| kbase | ror:01znn6x10 |  | Title: KBase<br>|
| osti | ror:031478740 |  | Title: OSTI<br>|
| ess_dive | ror:01t14bp54 |  | Title: ESS-DIVE<br>|
| massive | None |  | Title: MassIVE<br>|
| gsc | None |  | Title: GSC<br>|
| zenodo | None |  | Title: Zenodo<br>|
| edi | ror:0330j0z60 |  | Title: EDI<br>|
| figshare | ror:041mxqs23 |  | Title: Figshare<br>|




## Slots

| Name | Description |
| ---  | --- |
| [doi_provider](doi_provider.md) | The authority, or organization, the DOI is associated with |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema






## LinkML Source

<details>
```yaml
name: DoiProviderEnum
description: The authority, or organization, the DOI is associated with
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
permissible_values:
  emsl:
    text: emsl
    meaning: ror:04rc0xn13
    title: EMSL
    aliases:
    - Environmental Molecular Sciences Laboratory
    - EMSL
  jgi:
    text: jgi
    meaning: ror:04xm1d337
    title: JGI
    aliases:
    - Joint Genome Institute
    - JGI
  kbase:
    text: kbase
    meaning: ror:01znn6x10
    title: KBase
    aliases:
    - KBase
  osti:
    text: osti
    meaning: ror:031478740
    title: OSTI
    aliases:
    - Office of Scientific and Technical Information
    - OSTI
  ess_dive:
    text: ess_dive
    meaning: ror:01t14bp54
    title: ESS-DIVE
    aliases:
    - ESS-DIVE
    - Environmental System Science Data Infrastructure for a Virtual Ecosystem
  massive:
    text: massive
    title: MassIVE
    aliases:
    - MassIVE
    - Mass Spectrometry Virtual Environment
  gsc:
    text: gsc
    title: GSC
    aliases:
    - GSC
    - Genomic Standards Consortium
  zenodo:
    text: zenodo
    title: Zenodo
    aliases:
    - Zenodo
  edi:
    text: edi
    meaning: ror:0330j0z60
    title: EDI
    aliases:
    - EDI
    - Environmental Data Initiative
  figshare:
    text: figshare
    meaning: ror:041mxqs23
    title: Figshare

```
</details>