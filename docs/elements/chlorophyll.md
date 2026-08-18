

# Slot: chlorophyll (chlorophyll) 


_Concentration of chlorophyll (Unit: mg/m3 or ug/L)_





URI: [basalt_schema:chlorophyll](https://emsl-computing.github.io/BASALT-Schema/elements/chlorophyll)
Alias: chlorophyll

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
| Regex Pattern | `^\d+(\.\d+)?\s*(mg/m3|ug/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:chlorophyll |
| native | basalt_schema:chlorophyll |




## LinkML Source

<details>
```yaml
name: chlorophyll
description: 'Concentration of chlorophyll (Unit: mg/m3 or ug/L)'
title: chlorophyll
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: chlorophyll
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(mg/m3|ug/L)$

```
</details>