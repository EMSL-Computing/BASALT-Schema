

# Slot: calcium (calcium) 


_Concentration of calcium in the sample (Unit: mg/L or umol/L or ppm)_





URI: [basalt_schema:calcium](https://emsl-computing.github.io/BASALT-Schema/elements/calcium)
Alias: calcium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [SedimentSample](SedimentSample.md) | A sample of sediment collected from the environment |  no  |
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
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/L|umol/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:calcium |
| native | basalt_schema:calcium |




## LinkML Source

<details>
```yaml
name: calcium
description: 'Concentration of calcium in the sample (Unit: mg/L or umol/L or ppm)'
title: calcium
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: calcium
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/L|umol/L|ppm)$

```
</details>