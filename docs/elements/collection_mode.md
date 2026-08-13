

# Slot: collection_mode 


_The collection mode for the mass spectrometry data (e.g., profile, centroid)_





URI: [basalt_schema:collection_mode](https://EMSL-Computing.github.io/BASALT-Schema/collection_mode)
Alias: collection_mode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) | Raw data files output from a mass spectrometry instrument |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrumCollectionModeEnum](MassSpectrumCollectionModeEnum.md) |
| Domain Of | [MassSpectrometryInstrumentData](MassSpectrometryInstrumentData.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:collection_mode |
| native | basalt_schema:collection_mode |




## LinkML Source

<details>
```yaml
name: collection_mode
description: The collection mode for the mass spectrometry data (e.g., profile, centroid)
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: collection_mode
domain_of:
- MassSpectrometryInstrumentData
range: MassSpectrumCollectionModeEnum

```
</details>