

# Slot: soil texture (soil_texture) 


_The relative proportion of different grain sizes of mineral particles in a soil as described using a standard system; express as decimal percent sand (50 um to 2 mm) silt (2 um to 50 um) and clay (<2 um) with optional textural name (e.g. sand:0.20 silt:0.25 clay:0.55 description:silty clay loam)._





URI: [basalt_schema:soil_texture](https://EMSL-Computing.github.io/BASALT-Schema/soil_texture)
Alias: soil_texture

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [SoilSample](SoilSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^(\w+:0\.\d+ )*description:[A-Za-z ]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soil_texture |
| native | basalt_schema:soil_texture |




## LinkML Source

<details>
```yaml
name: soil_texture
description: The relative proportion of different grain sizes of mineral particles
  in a soil as described using a standard system; express as decimal percent sand
  (50 um to 2 mm) silt (2 um to 50 um) and clay (<2 um) with optional textural name
  (e.g. sand:0.20 silt:0.25 clay:0.55 description:silty clay loam).
title: soil texture
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: soil_texture
domain_of:
- SoilSample
range: string
pattern: ^(\w+:0\.\d+ )*description:[A-Za-z ]+$

```
</details>