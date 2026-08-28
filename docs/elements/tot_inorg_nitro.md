

# Slot: total inorganic nitrogen (tot_inorg_nitro) 


_Total inorganic nitrogen content. (Unit: ug/L)_





URI: [basalt_schema:tot_inorg_nitro](https://emsl-computing.github.io/BASALT-Schema/elements/tot_inorg_nitro)
Alias: tot_inorg_nitro

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
| Regex Pattern | `^\d+(\.\d+)?\s*(ug/L)$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:tot_inorg_nitro |
| native | basalt_schema:tot_inorg_nitro |




## LinkML Source

<details>
```yaml
name: tot_inorg_nitro
description: 'Total inorganic nitrogen content. (Unit: ug/L)'
title: total inorganic nitrogen
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: tot_inorg_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(ug/L)$

```
</details>