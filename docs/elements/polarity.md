

# Slot: polarity 


_Polarity setting used in the mass spectrometry method_





URI: [basalt_schema:polarity](https://EMSL-Computing.github.io/basalt-schema/polarity)
Alias: polarity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PolarityEnum](PolarityEnum.md) |
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
| self | basalt_schema:polarity |
| native | basalt_schema:polarity |




## LinkML Source

<details>
```yaml
name: polarity
description: Polarity setting used in the mass spectrometry method
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: polarity
domain_of:
- MassSpectrometryConfiguration
range: PolarityEnum
required: true

```
</details>