

# Slot: uses_calibration 


_Reference to the raw data file from the standard which was run with a batch of samples that was used as calibration for this data processing workflow run._





URI: [analysis_api_schema:uses_calibration](https://w3id.org/MONet/analysis-api-schema/uses_calibration)
Alias: uses_calibration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) |
| Domain Of | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/analysis-api-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | analysis_api_schema:uses_calibration |
| native | analysis_api_schema:uses_calibration |




## LinkML Source

<details>
```yaml
name: uses_calibration
description: Reference to the raw data file from the standard which was run with a
  batch of samples that was used as calibration for this data processing workflow
  run.
from_schema: https://w3id.org/MONet/analysis-api-schema
rank: 1000
alias: uses_calibration
domain_of:
- MassSpectrometryDataProcessingActivity
range: MassSpectrometryStandardRun

```
</details>