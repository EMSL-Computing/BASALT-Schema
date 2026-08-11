

# Slot: uses_raw_ms_data 


_The raw data file, output by a mass spectrometer, that was analyzed in  this data processing workflow run._





URI: [basalt_schema:uses_raw_ms_data](https://EMSL-Computing.github.io/basalt-schema/uses_raw_ms_data)
Alias: uses_raw_ms_data

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) | Concrete mass spectrometry workflow run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |
| Domain Of | [MassSpectrometryDataProcessingActivity](MassSpectrometryDataProcessingActivity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:uses_raw_ms_data |
| native | basalt_schema:uses_raw_ms_data |




## LinkML Source

<details>
```yaml
name: uses_raw_ms_data
description: The raw data file, output by a mass spectrometer, that was analyzed in  this
  data processing workflow run.
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: uses_raw_ms_data
domain_of:
- MassSpectrometryDataProcessingActivity
range: MassSpectrometryInstrumentData

```
</details>