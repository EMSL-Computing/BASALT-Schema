

# Slot: tidal stage (tidal_stage) 


_Stage of tide_





URI: [basalt_schema:tidal_stage](https://EMSL-Computing.github.io/basalt-schema/tidal_stage)
Alias: tidal_stage

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [TidalStageEnum](TidalStageEnum.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tidal_stage |
| native | basalt_schema:tidal_stage |




## LinkML Source

<details>
```yaml
name: tidal_stage
description: Stage of tide
title: tidal stage
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: tidal_stage
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: TidalStageEnum

```
</details>