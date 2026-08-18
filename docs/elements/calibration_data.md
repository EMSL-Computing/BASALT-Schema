

# Slot: calibration_data 


_Reference to the raw instrument data file used for calibration_





URI: [basalt_schema:calibration_data](https://EMSL-Computing.github.io/BASALT-Schema/calibration_data)
Alias: calibration_data

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) | A record of a mass spectrometry standard run with a batch of samples, which i... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |
| Domain Of | [MassSpectrometryStandardRun](MassSpectrometryStandardRun.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:calibration_data |
| native | basalt_schema:calibration_data |




## LinkML Source

<details>
```yaml
name: calibration_data
description: Reference to the raw instrument data file used for calibration
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: calibration_data
domain_of:
- MassSpectrometryStandardRun
range: MassSpectrometryInstrumentData

```
</details>