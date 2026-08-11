

# Slot: uses_chromatography 


_Points to a record of the chromatography used to introduce samples for the mass spectrometry run._





URI: [basalt_schema:uses_chromatography](https://EMSL-Computing.github.io/basalt-schema/uses_chromatography)
Alias: uses_chromatography

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChromatographyConfiguration](ChromatographyConfiguration.md) |
| Domain Of | [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:uses_chromatography |
| native | basalt_schema:uses_chromatography |




## LinkML Source

<details>
```yaml
name: uses_chromatography
description: Points to a record of the chromatography used to introduce samples for
  the mass spectrometry run.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: uses_chromatography
domain_of:
- MassSpectrometryDataGenerationActivity
range: ChromatographyConfiguration

```
</details>