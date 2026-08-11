

# Slot: mean friction velocity (mean_frict_vel) 


_Measurement of mean friction velocity (Unit: m/s)_





URI: [basalt_schema:mean_frict_vel](https://EMSL-Computing.github.io/basalt-schema/mean_frict_vel)
Alias: mean_frict_vel

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
| Regex Pattern | `^\d+(\.\d+)?\s*m/s$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:mean_frict_vel |
| native | basalt_schema:mean_frict_vel |




## LinkML Source

<details>
```yaml
name: mean_frict_vel
description: 'Measurement of mean friction velocity (Unit: m/s)'
title: mean friction velocity
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: mean_frict_vel
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*m/s$

```
</details>