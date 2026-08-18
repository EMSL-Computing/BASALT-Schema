

# Slot: bromide (bromide) 


_Concentration of bromide (Unit: ppm)_





URI: [basalt_schema:bromide](https://emsl-computing.github.io/BASALT-Schema/elements/bromide)
Alias: bromide

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
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*ppm$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:bromide |
| native | basalt_schema:bromide |




## LinkML Source

<details>
```yaml
name: bromide
description: 'Concentration of bromide (Unit: ppm)'
title: bromide
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: bromide
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*ppm$

```
</details>