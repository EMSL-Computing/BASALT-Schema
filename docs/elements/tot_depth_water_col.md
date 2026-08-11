

# Slot: total depth of water column (tot_depth_water_col) 


_Measurement of total depth of water column (Unit: m)_





URI: [basalt_schema:tot_depth_water_col](https://w3id.org/MONet/basalt-schema/tot_depth_water_col)
Alias: tot_depth_water_col

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*m$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/MONet/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_depth_water_col |
| native | basalt_schema:tot_depth_water_col |




## LinkML Source

<details>
```yaml
name: tot_depth_water_col
description: 'Measurement of total depth of water column (Unit: m)'
title: total depth of water column
from_schema: https://w3id.org/MONet/basalt-schema
rank: 1000
alias: tot_depth_water_col
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*m$

```
</details>