

# Slot: dd_ms2_resolution 


_Data-dependent MS2 resolution setting used in the mass spectrometry method_





URI: [basalt_schema:dd_ms2_resolution](https://EMSL-Computing.github.io/basalt-schema/dd_ms2_resolution)
Alias: dd_ms2_resolution

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Double](Double.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:dd_ms2_resolution |
| native | basalt_schema:dd_ms2_resolution |




## LinkML Source

<details>
```yaml
name: dd_ms2_resolution
description: Data-dependent MS2 resolution setting used in the mass spectrometry method
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: dd_ms2_resolution
domain_of:
- MassSpectrometryConfiguration
range: double
required: true

```
</details>