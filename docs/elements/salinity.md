

# Slot: salinity (salinity) 


_Salinity is the total concentration of all dissolved salts in a sample. While salinity can be measured by a complete chemical analysis, this method is difficult and time consuming. More often it is instead derived from the conductivity measurement. This is known as practical salinity. These derivations compare the specific conductance of the sample to a salinity standard such as seawater (Unit: practical salinity unit or percent)_





URI: [basalt_schema:salinity](https://emsl-computing.github.io/BASALT-Schema/elements/salinity)
Alias: salinity

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | A sample containing plant material |  no  |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [PlantSample](PlantSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(practical salinity unit|percent)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:salinity |
| native | basalt_schema:salinity |




## LinkML Source

<details>
```yaml
name: salinity
description: 'Salinity is the total concentration of all dissolved salts in a sample.
  While salinity can be measured by a complete chemical analysis, this method is difficult
  and time consuming. More often it is instead derived from the conductivity measurement.
  This is known as practical salinity. These derivations compare the specific conductance
  of the sample to a salinity standard such as seawater (Unit: practical salinity
  unit or percent)'
title: salinity
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: salinity
domain_of:
- OtherUndescribedSample
- PlantSample
- SedimentSample
- SoilSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(practical salinity unit|percent)$

```
</details>