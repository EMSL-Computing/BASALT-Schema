

# Slot: dissolved oxygen (diss_oxygen) 


_Concentration of dissolved oxygen. (Unit: umol/kg or mg/L)_





URI: [basalt_schema:diss_oxygen](https://emsl-computing.github.io/BASALT-Schema/elements/diss_oxygen)
Alias: diss_oxygen

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/kg|mg/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_oxygen |
| native | basalt_schema:diss_oxygen |




## LinkML Source

<details>
```yaml
name: diss_oxygen
description: 'Concentration of dissolved oxygen. (Unit: umol/kg or mg/L)'
title: dissolved oxygen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: diss_oxygen
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/kg|mg/L)$

```
</details>