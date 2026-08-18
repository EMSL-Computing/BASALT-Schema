

# Slot: acquisition_strategy 


_The acquisition strategy used in the mass spectrometry run._





URI: [basalt_schema:acquisition_strategy](https://emsl-computing.github.io/BASALT-Schema/elements/acquisition_strategy)
Alias: acquisition_strategy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpectrometryAcquisitionStrategyEnum](MassSpectrometryAcquisitionStrategyEnum.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:acquisition_strategy |
| native | basalt_schema:acquisition_strategy |




## LinkML Source

<details>
```yaml
name: acquisition_strategy
description: The acquisition strategy used in the mass spectrometry run.
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: acquisition_strategy
domain_of:
- MassSpectrometryConfiguration
range: MassSpectrometryAcquisitionStrategyEnum

```
</details>