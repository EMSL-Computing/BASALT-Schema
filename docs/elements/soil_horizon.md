

# Slot: soil horizon (soil_horizon) 


_Specific layer in the land area which measures parallel to the soil surface and possesses physical characteristics which differ from the layers above and beneath._





URI: [basalt_schema:soil_horizon](https://EMSL-Computing.github.io/BASALT-Schema/soil_horizon)
Alias: soil_horizon

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SoilHorizonEnum](SoilHorizonEnum.md) |
| Domain Of | [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soil_horizon |
| native | basalt_schema:soil_horizon |
| exact | MIXS:0001082 |




## LinkML Source

<details>
```yaml
name: soil_horizon
description: Specific layer in the land area which measures parallel to the soil surface
  and possesses physical characteristics which differ from the layers above and beneath.
title: soil horizon
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
exact_mappings:
- MIXS:0001082
rank: 1000
alias: soil_horizon
domain_of:
- SoilSample
range: SoilHorizonEnum

```
</details>