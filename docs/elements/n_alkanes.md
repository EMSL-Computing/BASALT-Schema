

# Slot: n-alkanes (n_alkanes) 


_Concentration of n-alkanes; can include multiple n-alkanes (Unit: ug/mL)_





URI: [basalt_schema:n_alkanes](https://emsl-computing.github.io/BASALT-Schema/elements/n_alkanes)
Alias: n_alkanes

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










## Identifier and Mapping Information





### Schema Source


* from schema: https://emsl-computing.github.io/BASALT-Schema




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | basalt_schema:n_alkanes |
| native | basalt_schema:n_alkanes |




## LinkML Source

<details>
```yaml
name: n_alkanes
description: 'Concentration of n-alkanes; can include multiple n-alkanes (Unit: ug/mL)'
title: n-alkanes
from_schema: https://emsl-computing.github.io/BASALT-Schema
rank: 1000
alias: n_alkanes
domain_of:
- OtherUndescribedSample
- SedimentSample
- WaterSample
range: string

```
</details>