

# Slot: loop_count 


_Number of MS2 scans to be acquired between each full MS scan._





URI: [basalt_schema:loop_count](https://emsl-computing.github.io/BASALT-Schema/elements/loop_count)
Alias: loop_count

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:loop_count |
| native | basalt_schema:loop_count |




## LinkML Source

<details>
```yaml
name: loop_count
description: Number of MS2 scans to be acquired between each full MS scan.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: loop_count
domain_of:
- MassSpectrometryConfiguration
range: string
required: true

```
</details>