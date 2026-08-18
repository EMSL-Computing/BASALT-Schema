

# Slot: uses_calibration 


_Reference to the raw data file from the standard which was run with a batch of samples that was used as calibration for this data processing workflow run._





URI: [basalt_schema:uses_calibration](https://EMSL-Computing.github.io/BASALT-Schema/uses_calibration)
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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:uses_calibration |
| native | basalt_schema:uses_calibration |




## LinkML Source

<details>
```yaml
name: uses_calibration
description: Reference to the raw data file from the standard which was run with a
  batch of samples that was used as calibration for this data processing workflow
  run.
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: uses_calibration
domain_of:
- MassSpectrometryDataProcessingActivity
range: MassSpectrometryStandardRun

```
</details>