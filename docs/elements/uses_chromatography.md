

# Slot: uses_chromatography 


_Points to a record of the chromatography used to introduce samples for the mass spectrometry run._





URI: [analysis_api_schema:uses_chromatography](https://w3id.org/MONet/analysis-api-schema/uses_chromatography)
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


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:uses_chromatography |
| native | analysis_api_schema:uses_chromatography |




## LinkML Source

<details>
```yaml
name: uses_chromatography
description: Points to a record of the chromatography used to introduce samples for
  the mass spectrometry run.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: uses_chromatography
domain_of:
- MassSpectrometryDataGenerationActivity
range: ChromatographyConfiguration

```
</details>