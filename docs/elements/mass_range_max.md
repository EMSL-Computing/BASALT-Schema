

# Slot: mass_range_max 


_The maximum mass observable by this run (in m/z)._





URI: [basalt_schema:mass_range_max](https://EMSL-Computing.github.io/basalt-schema/mass_range_max)
Alias: mass_range_max

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:mass_range_max |
| native | basalt_schema:mass_range_max |




## LinkML Source

<details>
```yaml
name: mass_range_max
description: The maximum mass observable by this run (in m/z).
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: mass_range_max
domain_of:
- MassSpectrometryConfiguration
range: float

```
</details>