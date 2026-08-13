

# Slot: carbon nitrogen ratio (carb_nitro_ratio) 


_Ratio of amount or concentrations of carbon to nitrogen._





URI: [basalt_schema:carb_nitro_ratio](https://EMSL-Computing.github.io/BASALT-Schema/carb_nitro_ratio)
Alias: carb_nitro_ratio

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:carb_nitro_ratio |
| native | basalt_schema:carb_nitro_ratio |




## LinkML Source

<details>
```yaml
name: carb_nitro_ratio
description: Ratio of amount or concentrations of carbon to nitrogen.
title: carbon nitrogen ratio
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: carb_nitro_ratio
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>