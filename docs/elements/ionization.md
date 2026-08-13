

# Slot: ionization 


_Type of ionization used in the mass spectrometry method_





URI: [basalt_schema:ionization](https://EMSL-Computing.github.io/BASALT-Schema/ionization)
Alias: ionization

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IonizationSourceEnum](IonizationSourceEnum.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ionization |
| native | basalt_schema:ionization |




## LinkML Source

<details>
```yaml
name: ionization
description: Type of ionization used in the mass spectrometry method
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: ionization
domain_of:
- MassSpectrometryConfiguration
range: IonizationSourceEnum
required: true

```
</details>