

# Slot: uses_ms_configuration 


_Points to a record of the configuration used for the mass spectrometry run._





URI: [analysis_api_schema:uses_ms_configuration](https://w3id.org/MONet/analysis-api-schema/uses_ms_configuration)
Alias: uses_ms_configuration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) | A record of the mass spectrometry run that generates a raw data product |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |
| Domain Of | [MassSpectrometryDataGenerationActivity](MassSpectrometryDataGenerationActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:uses_ms_configuration |
| native | analysis_api_schema:uses_ms_configuration |




## LinkML Source

<details>
```yaml
name: uses_ms_configuration
description: Points to a record of the configuration used for the mass spectrometry
  run.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: uses_ms_configuration
domain_of:
- MassSpectrometryDataGenerationActivity
range: MassSpectrometryConfiguration
required: true

```
</details>