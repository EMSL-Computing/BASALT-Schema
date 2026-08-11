

# Slot: pH (ph) 


_pH measurement of the sample or liquid portion of sample or aqueous phase of the fluid_





URI: [basalt_schema:ph](https://EMSL-Computing.github.io/basalt-schema/ph)
Alias: ph

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SoilSample](SoilSample.md) | A sample of soil collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [PHProduct](PHProduct.md) | Soil pH analysis product, typically derived via pH meter or similar instrumen... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [PHProduct](PHProduct.md), [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [SoilSample](SoilSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:ph |
| native | basalt_schema:ph |




## LinkML Source

<details>
```yaml
name: ph
description: pH measurement of the sample or liquid portion of sample or aqueous phase
  of the fluid
title: pH
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: ph
domain_of:
- pHProduct
- OtherUndescribedSample
- SedimentSample
- SoilSample
- WaterSample
range: float

```
</details>