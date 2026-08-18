

# Slot: soluble reactive phosphorus (soluble_react_phosp) 


_Concentration of soluble reactive phosphorus. (Unit: umol/L or mg/L or ppm)_





URI: [basalt_schema:soluble_react_phosp](https://emsl-computing.github.io/BASALT-Schema/elements/soluble_react_phosp)
Alias: soluble_react_phosp

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OtherUndescribedSample](OtherUndescribedSample.md), [WaterSample](WaterSample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:soluble_react_phosp |
| native | basalt_schema:soluble_react_phosp |




## LinkML Source

<details>
```yaml
name: soluble_react_phosp
description: 'Concentration of soluble reactive phosphorus. (Unit: umol/L or mg/L
  or ppm)'
title: soluble reactive phosphorus
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: soluble_react_phosp
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|mg/L|ppm)$

```
</details>