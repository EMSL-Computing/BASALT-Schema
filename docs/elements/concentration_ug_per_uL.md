

# Slot: concentration (ug/uL) (concentration_ug_per_uL) 


_Concentration of the substance in micrograms per microliter._





URI: [basalt_schema:concentration_ug_per_uL](https://emsl-computing.github.io/BASALT-Schema/elements/concentration_ug_per_uL)
Alias: concentration_ug_per_uL

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CoreSection](CoreSection.md) | A section of a core sample (TOP, MID, BTM) |  no  |
| [ProcessedSample](ProcessedSample.md) | A sample that has undergone processing or analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ProcessedSample](ProcessedSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:concentration_ug_per_uL |
| native | basalt_schema:concentration_ug_per_uL |




## LinkML Source

<details>
```yaml
name: concentration_ug_per_uL
description: Concentration of the substance in micrograms per microliter.
title: concentration (ug/uL)
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: concentration_ug_per_uL
domain_of:
- ProcessedSample
range: float

```
</details>