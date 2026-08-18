

# Slot: resolution 



URI: [basalt_schema:resolution](https://emsl-computing.github.io/BASALT-Schema/elements/resolution)
Alias: resolution

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MassSpectrometryConfiguration](MassSpectrometryConfiguration.md) | Instrument configuration and setup for a mass spectrometry run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MassSpecResolutionEnum](MassSpecResolutionEnum.md) |
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
| self | basalt_schema:resolution |
| native | basalt_schema:resolution |




## LinkML Source

<details>
```yaml
name: resolution
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: resolution
domain_of:
- MassSpectrometryConfiguration
range: MassSpecResolutionEnum
required: true

```
</details>