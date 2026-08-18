

# Slot: aluminum saturation (al_sat) 


_Aluminum saturation (esp. For tropical soils)_





URI: [basalt_schema:al_sat](https://emsl-computing.github.io/BASALT-Schema/elements/al_sat)
Alias: al_sat

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  yes  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:al_sat |
| native | basalt_schema:al_sat |




## LinkML Source

<details>
```yaml
name: al_sat
description: Aluminum saturation (esp. For tropical soils)
title: aluminum saturation
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: al_sat
domain_of:
- OtherUndescribedSample
- SoilSample
range: string

```
</details>