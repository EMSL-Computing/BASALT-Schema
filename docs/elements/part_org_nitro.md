

# Slot: particulate organic nitrogen (part_org_nitro) 


_Concentration of particulate organic nitrogen. (Unit: ug/L or umol/L)_





URI: [basalt_schema:part_org_nitro](https://emsl-computing.github.io/BASALT-Schema/elements/part_org_nitro)
Alias: part_org_nitro

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
| Regex Pattern | `^\d+(\.\d+)?\s*(umol/L|ug/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:part_org_nitro |
| native | basalt_schema:part_org_nitro |




## LinkML Source

<details>
```yaml
name: part_org_nitro
description: 'Concentration of particulate organic nitrogen. (Unit: ug/L or umol/L)'
title: particulate organic nitrogen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: part_org_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ug/L)$

```
</details>