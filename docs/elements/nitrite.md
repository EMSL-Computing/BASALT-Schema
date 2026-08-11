

# Slot: nitrite (nitrite) 


_Concentration of nitrite in the sample (Unit: umol/L or mg/L or ppm)_





URI: [basalt_schema:nitrite](https://EMSL-Computing.github.io/basalt-schema/nitrite)
Alias: nitrite

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
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [SedimentSample](SedimentSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://EMSL-Computing.github.io/basalt-schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:nitrite |
| native | basalt_schema:nitrite |




## LinkML Source

<details>
```yaml
name: nitrite
description: 'Concentration of nitrite in the sample (Unit: umol/L or mg/L or ppm)'
title: nitrite
from_schema: https://EMSL-Computing.github.io/basalt-schema
rank: 1000
alias: nitrite
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>