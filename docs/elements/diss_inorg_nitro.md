

# Slot: dissolved inorganic nitrogen (diss_inorg_nitro) 


_Concentration of dissolved inorganic nitrogen. (Unit: ug/L or umol/L)_





URI: [basalt_schema:diss_inorg_nitro](https://EMSL-Computing.github.io/BASALT-Schema/diss_inorg_nitro)
Alias: diss_inorg_nitro

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [WaterSample](WaterSample.md) | A sample of water collected from the environment |  no  |
| [OtherUndescribedSample](OtherUndescribedSample.md) | A sample that does not fit into any of the other described sample types |  no  |






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


* from schema: https://EMSL-Computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:diss_inorg_nitro |
| native | basalt_schema:diss_inorg_nitro |




## LinkML Source

<details>
```yaml
name: diss_inorg_nitro
description: 'Concentration of dissolved inorganic nitrogen. (Unit: ug/L or umol/L)'
title: dissolved inorganic nitrogen
from_schema: https://EMSL-Computing.github.io/BASALT-Schema
rank: 1000
alias: diss_inorg_nitro
domain_of:
- OtherUndescribedSample
- WaterSample
range: string
pattern: ^\d+(\.\d+)?\s*(umol/L|ug/L)$

```
</details>