

# Slot: duration_min 


_how long something took, in minutes_





URI: [basalt_schema:duration_min](https://emsl-computing.github.io/BASALT-Schema/elements/duration_min)
Alias: duration_min

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MobilePhaseSegment](MobilePhaseSegment.md) | A segment of the mobile phase used in chromatography during mass spectrometry |  no  |
| [ChemicalConversionProcess](ChemicalConversionProcess.md) | A chemical conversion process used in sample preparation |  no  |
| [ChromatographyConfiguration](ChromatographyConfiguration.md) | Configuration and settings for a chromatography run |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ChromatographyConfiguration](ChromatographyConfiguration.md), [MobilePhaseSegment](MobilePhaseSegment.md), [ChemicalConversionProcess](ChemicalConversionProcess.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:duration_min |
| native | basalt_schema:duration_min |




## LinkML Source

<details>
```yaml
name: duration_min
description: how long something took, in minutes
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: duration_min
domain_of:
- ChromatographyConfiguration
- MobilePhaseSegment
- ChemicalConversionProcess
range: float

```
</details>