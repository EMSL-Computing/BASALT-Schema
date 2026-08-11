

# Slot: ms_raw_file_type 


_the filetype of the mass spectrometry instrument data_





URI: [basalt_schema:ms_raw_file_type](https://EMSL-Computing.github.io/basalt-schema/ms_raw_file_type)
Alias: ms_raw_file_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) | Raw data files output from a mass spectrometry instrument |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpecRawFileTypeEnum](MassSpecRawFileTypeEnum.md) |
| Domain Of | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ms_raw_file_type |
| native | basalt_schema:ms_raw_file_type |




## LinkML Source

<details>
```yaml
name: ms_raw_file_type
description: the filetype of the mass spectrometry instrument data
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: ms_raw_file_type
domain_of:
- MassSpectrometryInstrumentData
range: MassSpecRawFileTypeEnum

```
</details>